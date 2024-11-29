<<<<<<< HEAD
function [value] = binaryBanditB(action)
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
% For help on usage type >>help binaryBanditB
%
% >> binaryBanditB(action)
%----------------------------------------------

% Define success probabilities for actions
p = [.8 .9]; % Probabilities for binaryBanditB
if rand < p(action)
    value = 1; % Success
else
    value = 0; % Failure
end
end
=======
function [value] = binaryBanditB(action)
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
% For help on usage type >>help binaryBanditB
%
% >> binaryBanditB(action)
%----------------------------------------------

% Define success probabilities for actions
p = [.8 .9]; % Probabilities for binaryBanditB
if rand < p(action)
    value = 1; % Success
else
    value = 0; % Failure
end
end
>>>>>>> c233d70a206ccb7319170a0a637b305b3060019a
