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

Horizon = 30;  %30ms - window length
OrderLPC = 24;   %order of LPC
Buffer = 0;    % initialization
out = zeros(size(sig)); % initialization

Horizon = Horizon*Fs/1000;
Shift = Horizon/2;       % frame size - step size
Win = hanning(Horizon);  % analysis window

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
  ex = filter([0 -a(2:end)],1,sigLPC);
  % gain
  plot(1:100,sigLPC(end-100+1:end),1:100,ex(end-100+1:end),'--');grid;xlabel('Sample Number');ylabel('Amplitude');legend('Original signal','LPC estimate')
  % synthesis
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

