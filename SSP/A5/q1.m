[sig, Fs]=audioread('q1.wav')
plot(sig)

Horizon = 30
Buffer = 0;    % initialization
OrderLPC = 8
out = zeros(size(sig))

Horizon = Horizon*Fs/1000;
Shift = Horizon/2;
Win = hanning(Horizon)

Lsig = length(sig);
slice = 1:Horizon;
tosave = 1:Shift;
Nfr = floor((Lsig-Horizon)/Shift)+1;  % number of frames

for i=1:Nfr
    x = Win*.sig(slice)
    
    slice = slice+Shift;   % move the frame
    tosave = tosave+Shift;
end