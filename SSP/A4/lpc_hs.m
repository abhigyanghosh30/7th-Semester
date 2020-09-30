function out = lpc_try(file)
%
% INPUT:
%   file: input filename of a wav file
% OUTPUT:
%   out: a vector contaning the output signal
%
% Example:
%   
%   out = lpc_try('yourname.wav');
%   [sig,fs]= audioread('yourname.wav');
%   sound(out,fs);
%   sound(sig,fs);
%   sound([out [zeros(2000,1);sig(1:length(sig)-2000)]],fs); % create echo
%
%
% LP analysis code starts here
    [sig, fs] = audioread(file);
    sig = sig(:,1);
    sig = resample(sig,16000,fs);
    fs = 16000;
    
    Horizon = 30;  %30ms - window length
    OrderLPC = 24;   %order of LPC
    Buffer = 0;    % initialization
    out = zeros(size(sig)); % initialization
    
    Horizon = Horizon*fs/1000; %frame size 
    Shift = Horizon/2;       % frame size - step size/ overlap
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
      r = xcorr(sigLPC); % correlation
      [a,G] =  lpc(r, OrderLPC);% LPC coef.
      ex =  filter([0 -a(2:end)],1,sigLPC);% inverse filter
      t = tiledlayout(1,1);
      nexttile
      plot(1:512,f1(1:512),1:512,f2(1:512),'--');grid;xlabel('Sample Number');ylabel('Amplitude');legend('FFT','FREQZ')
      exportgraphics(t,sprintf('plots/plot_%d.png',l),'Resolution',300)
    %   disp(size(a));
    %   disp(size(G));
      % synthesis
      s = filter(G, a, ex);
      ens = sum(s.^2);   % get the short-time energy of the output
      g = sqrt(en/ens);  % normalization factor
      s  =s*g;           % energy compensation
      s(1:Shift) = s(1:Shift) + Buffer;  % Overlap and add
      out(tosave) = s(1:Shift);           % save the first part of the frame
      Buffer = s(Shift+1:Horizon);       % buffer the rest of the frame
      
      slice = slice+Shift;   % move the frame
      tosave = tosave+Shift;
      
    end
    
out = lpc_try('q1.wav');
audiowrite('q2_out.wav', out, fs);
% [sig, fs] = audioread('yourname.wav');
% sig = resample(sig,16000,fs);
% fs = 16000;
sound(out,fs);
sound(sig,fs);
