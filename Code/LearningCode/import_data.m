%% Import data from text file.
% Script for importing data from the following text file:
%
%    /Users/achattoraj/Dropbox/Up-stat/Data/year_wise/Finaldata_[2011].csv
%
% To extend the code to different selected data or a different text file,
% generate a function instead of a script.

% Auto-generated by MATLAB on 2018/03/30 12:17:06

%% Initialize variables.
%filename = '/Users/achattoraj/Dropbox/Up-stat/Data/year_wise/Finaldata_[2011].csv';
delimiter = ',';
startRow = 2;

%% Read columns of data as text:
% For more information, see the TEXTSCAN documentation.
formatSpec = '%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%[^\n\r]';

%% Open the text file.
fileID = fopen(filename,'r');

%% Read columns of data according to the format.
% This call is based on the structure of the file used to generate this
% code. If an error occurs for a different file, try regenerating the code
% from the Import Tool.
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter, 'HeaderLines' ,startRow-1, 'ReturnOnError', false, 'EndOfLine', '\r\n');

%% Close the text file.
fclose(fileID);

%% Convert the contents of columns containing numeric text to numbers.
% Replace non-numeric text with NaN.
raw = repmat({''},length(dataArray{1}),length(dataArray)-1);
for col=1:length(dataArray)-1
raw(1:length(dataArray{col}),col) = dataArray{col};
end
numericData = NaN(size(dataArray{1},1),size(dataArray,2));

for col=[1,2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
% Converts text in the input cell array to numbers. Replaced non-numeric
% text with NaN.
rawData = dataArray{col};
for row=1:size(rawData, 1);
% Create a regular expression to detect and remove non-numeric prefixes and
% suffixes.
regexstr = '(?<prefix>.*?)(?<numbers>([-]*(\d+[\,]*)+[\.]{0,1}\d*[eEdD]{0,1}[-+]*\d*[i]{0,1})|([-]*(\d+[\,]*)*[\.]{1,1}\d+[eEdD]{0,1}[-+]*\d*[i]{0,1}))(?<suffix>.*)';
try
result = regexp(rawData{row}, regexstr, 'names');
numbers = result.numbers;

% Detected commas in non-thousand locations.
invalidThousandsSeparator = false;
if any(numbers==',');
thousandsRegExp = '^\d+?(\,\d{3})*\.{0,1}\d*$';
if isempty(regexp(numbers, thousandsRegExp, 'once'));
numbers = NaN;
invalidThousandsSeparator = true;
end
end
% Convert numeric text to numbers.
if ~invalidThousandsSeparator;
numbers = textscan(strrep(numbers, ',', ''), '%f');
numericData(row, col) = numbers{1};
raw{row, col} = numbers{1};
end
catch me
end
end
end


%% Split data into numeric and cell columns.
rawNumericColumns = raw(:, [1,2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]);
rawCellColumns = raw(:, [7,8]);


%% Replace non-numeric cells with NaN
R = cellfun(@(x) ~isnumeric(x) && ~islogical(x),rawNumericColumns); % Find non-numeric cells
rawNumericColumns(R) = {NaN}; % Replace non-numeric cells

%% Allocate imported array to column variable names
X = cell2mat(rawNumericColumns(:, 1));
Y = cell2mat(rawNumericColumns(:, 2));
GeoID = cell2mat(rawNumericColumns(:, 3));
OccurredFrom_Time = cell2mat(rawNumericColumns(:, 4));
OccurredFrom_Date_Month = cell2mat(rawNumericColumns(:, 5));
Patrol_Beat = cell2mat(rawNumericColumns(:, 6));
Statute_Text = rawCellColumns(:, 1);
Location_Type = rawCellColumns(:, 2);
Geo_Section_Num = cell2mat(rawNumericColumns(:, 7));
IsLarceny = cell2mat(rawNumericColumns(:, 8));
IsBurglary = cell2mat(rawNumericColumns(:, 9));
IsMotorVehicleTheft = cell2mat(rawNumericColumns(:, 10));
IsRobbery = cell2mat(rawNumericColumns(:, 11));
IsAggravatedAssault = cell2mat(rawNumericColumns(:, 12));
IsMurder = cell2mat(rawNumericColumns(:, 13));
IsNonNegligentManslaughter = cell2mat(rawNumericColumns(:, 14));
Ismor = cell2mat(rawNumericColumns(:, 15));
Isnoon = cell2mat(rawNumericColumns(:, 16));
Isnight = cell2mat(rawNumericColumns(:, 17));
AvgTemp = cell2mat(rawNumericColumns(:, 18));
Snowfall = cell2mat(rawNumericColumns(:, 19));
Asian = cell2mat(rawNumericColumns(:, 20));
Black = cell2mat(rawNumericColumns(:, 21));
White = cell2mat(rawNumericColumns(:, 22));
Other = cell2mat(rawNumericColumns(:, 23));
PopDensity = cell2mat(rawNumericColumns(:, 24));
PropRate14 = cell2mat(rawNumericColumns(:, 25));
Unemployed = cell2mat(rawNumericColumns(:, 26));
OwnerPer = cell2mat(rawNumericColumns(:, 27));
RenterPer = cell2mat(rawNumericColumns(:, 28));
IsFall = cell2mat(rawNumericColumns(:, 29));
IsSpring = cell2mat(rawNumericColumns(:, 30));
IsSummer = cell2mat(rawNumericColumns(:, 31));
IsWinter = cell2mat(rawNumericColumns(:, 32));


%% Clear temporary variables
clearvars filename delimiter startRow formatSpec fileID dataArray ans raw col numericData rawData row regexstr result numbers invalidThousandsSeparator thousandsRegExp me rawNumericColumns rawCellColumns R;