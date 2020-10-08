[sig, Fs]=audioread('q1.wav')
subplot(3,1,1);plot([1:length(sig)]/Fs,sig);grid;title('Full Wave with VOP marked')

VOP = [0.02,0.42,0.52,0.72]

hold on
stem(VOP,[0.6,0.6,0.6,0.6]);
hold off

[f0,loc] = pitch(sig,Fs)
subplot(3,1,2);grid;plot(loc/Fs,f0);grid;title('Pitch/F_0')
hold on
stem(VOP,[1,1,1,1]*max(f0));
hold off

coeffs = mfcc(sig,Fs,'LogEnergy','Replace')
log_e = coeffs(:,1)
subplot(3,1,3);plot([1:length(log_e)]/100,log_e);grid;title('Change in Log Energy')
hold on
stem(VOP,[1,1,1,1]*max(log_e));
hold off

