
str_array = [string('2014, 2015, 2016, 2017') string('2013, 2013, 2013, 2016') string('2011, 2012, 2013, 2014')];
for i = 1:length(str_array)
    i
    clearvars -except str_array i;
    %filename = strcat('/Users/rupamacharyya/Dropbox/Up-stat/Data/year_wise/Finaldata_[',string(str_array(i)),'].csv');
    filename = strcat('/Users/achattoraj/Dropbox/Up-stat/Data/year_wise/Finaldata_[',string(str_array(i)),'].csv');
    import_data;
    feat=[White,Asian,AvgTemp,Black,OccurredFrom_Date_Month,Other,OwnerPer,PopDensity,PropRate14,Unemployed,RenterPer,Snowfall,IsWinter,IsSpring,IsSummer,IsFall];
    params={'White';'Asian';'AvgTemp';'Black';'OccurredFrom_Date_Month';'Other';'OwnerPer';'PopDensity';'PropRate';'Unemployed';'RenterPer';'Snowfall';'IsWinter';'IsSpring';'IsSummer';'IsFall'};
    idtmp=find(abs(mean(feat))>2);
    feat(:,idtmp)=(feat(:,idtmp)-repmat(mean(feat(:,idtmp)),size(feat,1),1))./repmat(std(feat(:,idtmp)),size(feat,1),1);

    %% change for each year
    result = gwr(IsBurglary(:),feat(:,:),X(:),Y(:));
    save(strcat('result_burglary_cumulative',string(str_array(i))),'result');

end