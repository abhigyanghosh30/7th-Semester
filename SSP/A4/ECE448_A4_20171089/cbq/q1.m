[y,Fs]=audioread('q1.wav');
subplot(4,1,1);plot(y);
title('Original Wave')
xlabel('time in millisecond');

y = y((Fs*0.82:Fs*0.85))
y=y/(1.01*abs(max(y)));
t=(1/Fs:1/Fs:(length(y)/Fs))*1000;
N=Fs*0.03+1;
w=rectwin(N);
y=w.*y;
P=10; % order of LPC
ycorr=xcorr(y);
ycorr=ycorr./(abs(max(ycorr)));
A=ycorr(1:P);
r=ycorr(2:(P+1));
A=toeplitz(A);
A=-inv(A);
L=A*r;
L=transpose(L);
LPCoeffs(1,1:length([1,L])) = [1,L];
y5=conv(y,LPCoeffs);
y5=y5(round(P/2):length(y5)-round(P/2)-1);
subplot(4,1,2);plot(t, y);
title('30 millisecond voiced speech segment');
xlabel('time in millisecond');
ylabel('amplitude');
subplot(4,1,3);plot(t, y5);
title('LP Residual');
xlabel('time in millisecond');
ylabel('amplitude');

sum1=0;autocorrelation=0;

y=y5;
for l=0:(length(y)-1)
sum1=0;
for u=1:(length(y)-l)
  s=y(u)*y(u+l);
  sum1=sum1+s;
end
autocor(l+1)=sum1;
end
kk=(1/Fs:1/Fs:(length(autocor)/Fs))*1000;

subplot(4,1,4);
plot(kk,autocor);
title('Autocorrelation of LP Residual')
xlabel('time in milliseconds');

auto=autocor(21:end);
[P_max,sample_no]=max(auto)
  pitch_freq_to=(20+sample_no)*(1/Fs)
  pitch_freq_fo=1/pitch_freq_to