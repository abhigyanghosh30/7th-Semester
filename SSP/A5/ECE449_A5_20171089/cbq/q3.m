[sig, Fs]=audioread('seriously.wav')
subplot(4,1,1);plot([1:length(sig)]/Fs,sig);title('Full Wave')
Horizon = 100
Horizon = Horizon*Fs/1000
x = sig(0.84*Fs:1*Fs)
subplot(4,1,2);plot([1:length(x)]/Fs,x);title('Part of Wave')
% x = filter([1,-1],1, x)
% subplot(4,1,2);plot(sig);title('Pre-emphasis')

a = lpc(x,24);
est_x = filter([0 -a(2:end)],1,x);
e = x-est_x;
subplot(4,1,3);plot(est_x);title('Estimated')

gvv = cumtrapz(e)
subplot(4,1,4);plot(gvv);title('GVV')