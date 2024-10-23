function [value] = binaryBanditA(action)
%----------------------------------------------
% Exercise: Evaluation vs. Instruction
% CS307 AI, IIITV
% Autumn 2024-25
% Author : Pratik Shah
% Ref: Reinforcement Learning, Sutton and Barto
%----------------------------------------------
% Two actions 1 and 2
% Rewards are stochastic 1-Success/ 0-Failure
%
% For help on usage type >>help binaryBanditA
%
% >> binaryBanditA(action)
%----------------------------------------------

% Define success probabilities for actions
p = [.1 .2]; % Probabilities for binaryBanditA
if rand < p(action)
    value = 1; % Success
else
    value = 0; % Failure
end
end
