%{
Author - Aayan Mahmood 
Date - 25/8/2026
Purpose - Models the ideal Brayton cycle for a gas turbine, analysing 
the effect of pressure ratio on thermal efficiency and specific net work 
output. 
%}

%% Variables

T1 = 288.15; % K ( 15 C ) 
rp = 5:1:40; % pressure ratio from 5-40
gamma = 1.4;
T3 = 1500; % Inlet temp peak temp
cp = 1005; % J/KgK, specific heat of air 
%%

T2 = T1 * rp .^((gamma-1)/(gamma));
T4 = T3 * (1./rp).^((gamma-1)/(gamma));
%%

wc = cp*(T2-T1);
wt = cp*(T3-T4);
w_net = wt-wc; 
qin = cp*(T3-T2);
eta = w_net ./ qin;

%% Plot

figure;

subplot(1,2,1);
plot(rp, eta);
xlabel('Pressure Ratio');
ylabel('Thermal Efficiency');
title('Efficiency vs Pressure Ratio');
grid on;

subplot(1,2,2);
plot(rp, w_net / 1000);
xlabel('Pressure Ratio');
ylabel('Specific Net Work kJkg^-1');
title('Specific Work vs Pressure Ratio');
grid on;
