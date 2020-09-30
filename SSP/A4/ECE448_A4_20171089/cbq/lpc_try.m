function out = lpc_try(file)
%
% INPUT:
%   file: input filename of a wav file
% OUTPUT:
%   out: a vector contaning the output signal
%
% Example:
%   
%   out = lpc_try('1_H.wav');
%   [sig,fs]= audioread('1_H.wav');
%   sound(out,fs);
%   sound(sig,fs);
%   sound([out [zeros(2000,1);sig(1:length(sig)-2000)]],fs); % create echo
%
%
% LP analysis code starts here
% 
%

[sig, Fs] = audioread(file);
sig = sig(:,1)
sig = resample(sig,16000,Fs);
Fs = 16000;

Horizon = 30;  %30ms - window length
OrderLPC = 1;   %order of LPC
Buffer = 0;    % initialization
out = zeros(size(sig)); % initialization

Horizon = Horizon*Fs/1000;
Shift = Horizon/2;       % frame size - step size
Win = hanning(Horizon);  % analysis window

% sig = sig(1:Horizon*100)

Lsig = length(sig);
slice = 1:Horizon;
tosave = 1:Shift;
Nfr = floor((Lsig-Horizon)/Shift)+1;  % number of frames
% analysis frame-by-frame
for l=1:Nfr
  
  sigLPC = Win.*sig(slice);
  en = sum(sigLPC.^2); % get the short - term energy of the input
  % LPC analysis
  r =  xcorr(sigLPC)% correlation
  [a,G] =  lpc(sigLPC,OrderLPC) % LPC coef.
  disp(G)
  ex = filter([0 -a(2:end)],1,sigLPC);
  % gain
  
  % synthesis
  subplot(2,1,2)
  f1 = abs(fft(sigLPC,1024))
  f2 = abs(freqz(ex))
  t = tiledlayout(2,1);
  ax1  = nexttile;
  plot(1:100,sigLPC(end-100+1:end),1:100,ex(end-100+1:end),'--');grid;xlabel(ax1,'Sample Number');ylabel(ax1,'Amplitude');legend('Original signal','LPC estimate')
  ax2 = nexttile;
  plot(1:512,f1(1:512),1:512,f2(1:512),'--');grid;xlabel(ax2,'Sample Number');ylabel(ax2,'Amplitude');legend('FFT','FREQZ')
  exportgraphics(t,sprintf('plots/plot_%d.png',l))
  s = filter(G,a, ex);
  ens = sum(s.^2);   % get the short-time energy of the output
  g = sqrt(en/ens);  % normalization factor
  s  =s*g;           % energy compensation
  s(1:Shift) = s(1:Shift) + Buffer;  % Overlap and add
  out(tosave) = s(1:Shift);           % save the first part of the frame
  Buffer = s(Shift+1:Horizon);       % buffer the rest of the frame
  
  slice = slice+Shift;   % move the frame
  tosave = tosave+Shift;
end
audiowrite(sprintf('q2_%d_out.wav',OrderLPC),out,Fs)
