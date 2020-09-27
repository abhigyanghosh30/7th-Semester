[y,Fs]=audioread('q1.wav');
subplot(4,1,1);plot(y);
title('Original Wave')
xlabel('time in millisecond');
y=y(200:439);
y=y/(1.01*abs(max(y)));
t=(1/Fs:1/Fs:(length(y)/Fs))*1000;
%y=y(241:400);
N=240;
w=rectwin(N);
y=y.*w;
P=10;
ycorr=xcorr(y);
ycorr=ycorr./(abs(max(ycorr)));
A=ycorr(1:P);
r=ycorr(2:(P+1));
A=toeplitz(A);
% r_t=transpose(r);
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
%for i=1:window_length
   for l=0:(length(y)-1)
    sum1=0;
    for u=1:(length(y)-l)
      s=y(u)*y(u+l);
      sum1=sum1+s;
    end
    autocor(l+1)=sum1;
  end
%end


%tt=1/Fs:1/Fs:(length(y)/Fs);
kk=(1/Fs:1/Fs:(length(autocor)/Fs))*1000;

subplot(4,1,4);
plot(kk,autocor);
title('Autocorrelation of LP Residual')
xlabel('time in milliseconds');

auto=autocor(21:240);
  max1=0;
  for uu=1:220
    if(auto(uu)>max1)
      max1=auto(uu);
      sample_no=uu;
    end
  end
  pitch_freq_to=(20+sample_no)*(1/Fs)
  pitch_freq_fo=1/pitch_freq_to