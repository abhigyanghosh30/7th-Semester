[sig, Fs]=audioread('q1.wav')
% subplot(4,1,1);plot([1:length(sig)]/Fs,sig);title('Full Wave')
Horizon = 100
Horizon = Horizon*Fs/1000
sig = sig(0.25*Fs:0.32*Fs)
subplot(4,1,1);plot([1:length(sig)]/Fs,sig);title('Part of Wave')
sig = filter([1,-1],1, sig)
subplot(4,1,2);plot(sig);title('Pre-emphasis')

a = lpc(sig,24);
est_x = filter([0 -a(2:end)],1,x);
e = x-est_x;
subplot(4,1,3);plot(est_x);title('Estimated')

gvv = cumtrapz(e)
subplot(4,1,4);plot(gvv);title('GVV')