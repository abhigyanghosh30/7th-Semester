clear, clc, close all

    [S,fs] = audioread('arctic_a0001.wav');
    S=resample(S,8000,fs);
    s=S(:,1);
    fs=8000;
    N=length(s);
    
    x=diff(s);
    x(end+1)=x(end);
    
%     getting lp residual and taking hilbert transform of that
    lpc_1=lpc(s,10);
    residual=filter(lpc_1,1,s);
    s_a=hilbert(residual);
    s_he=abs(s_a);

    %applying zero frequency filtering to the speech sample
    b=1;
    a=[1,-2,1];
    y1=filter(b,a,x);
    y2=filter(b,a,y1);
    
    %applying zff to Hilbert Envelope
    y1_he=filter(b,a,s_he);
    y2_he=filter(b,a,y1_he);

    %taking mean window
    M=5*fs/1000;
    
    %subtracting out the mean to extract the characteristics of
    %discontinuities i.e removing trend
    y3=y2;
    for k=1:3
        tt=filter(ones(M,1),1,y3)/M;
        y3=y3-tt;
        y3=y3/5;
    end
    
    %subtracting out the mean to extract the characteristics of
    %discontinuities i.e removing trend from HE
    y3_he=y2_he;
    for k=1:4
        tt=filter(ones(M,1),1,y3_he)/M;
        y3_he=y3_he-tt;
    end
    
    
    t1=(0:N-1)/fs;
    subplot(4,1,1)
    plot(t1,s)
    title('sound signal')

    subplot(4,1,3)
    plot(t1,y3)
    title('zero frequency filtered signal(after trend removal)')
    
    subplot(4,1,4)
    plot(t1,y3_he)
    title('ZFF of HE')
    
   

    subplot(4,1,2)
    plot(t1,s_he)
    title('hilbert envelope')