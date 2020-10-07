[sig, Fs]=audioread('q1.wav')
subplot(3,1,1);plot([1:length(sig)]/Fs,sig);title('Full Wave')
Horizon = 100
Horizon = Horizon*Fs/1000
sig = sig(0.15*Fs:0.15*Fs+Horizon)
subplot(3,1,2);plot([1:length(sig)]/Fs,sig);title('Part of Wave')
n = length(sig)
x = sig(2:n)-sig(1:n-1)

% n = length(x)
% y_1 = x_n
% y_1 = y_1(2:n) + 2*y_1(1:n-1)
% y_1 = y_1(2:n-1) - y_1(1:n-2)
% y_1 = cat(1,x_n(1:2),y_1) 
% y_2 = y_1
% y_2 = y_2(2:n) + 2*y_2(1:n-1)
% y_2 = y_2(2:n-1) - y_2(1:n-2)
% y_2 = cat(1,y_1(1:2),y_2)
% y = y_2 - sum(y_2,1)/n

y_1 = cumtrapz(cumtrapz(x))
y_2 = cumtrapz(cumtrapz(x))

m = floor(5*Fs/1000)

y = []
k = 1
for i=1+m:length(y_2)-m
    y(k)=y_2(i)-mean(y_2(i-m:i+m))
    k=k+1
end

subplot(3,1,3);plot([1:length(y)]/Fs,y);title('5ms mean subtracted ZFF')