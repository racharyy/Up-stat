
year = [2011 2012 2013 2014 2015 2016 2017];
for i = 1:length(year)
    i
    clearvars -except year i;
%     filename = strcat('/Users/rupamacharyya/Dropbox/Up-stat/Data/year_wise/Finaldata_[',num2str(year(i)),'].csv');
    filename = strcat('/Users/achattoraj/Dropbox/Up-stat/Data/year_wise/Finaldata_[',num2str(year(i)),'].csv');
    import_data;
    idx=randperm(size(Black,1));
    tr_dt=idx(1:round(0.8*size(Black,1)));
    te_dt=idx(round(0.8*size(Black,1))+1:end);
    feat=[White,Asian,AvgTemp,Black,OccurredFrom_Date_Month,Other,OwnerPer,PopDensity,PropRate14,Unemployed,RenterPer,Snowfall,IsWinter,IsSpring,IsSummer,IsFall];
    params={'White';'Asian';'AvgTemp';'Black';'OccurredFrom_Date_Month';'Other';'OwnerPer';'PopDensity';'PropRate';'Unemployed';'RenterPer';'Snowfall';'IsWinter';'IsSpring';'IsSummer';'IsFall'};
    idtmp=find(abs(mean(feat))>2);
    feat(:,idtmp)=(feat(:,idtmp)-repmat(mean(feat(:,idtmp)),size(feat,1),1))./repmat(std(feat(:,idtmp)),size(feat,1),1);

    %% change for each year
    result = gwr(IsRobbery(tr_dt),feat(tr_dt,:),X(tr_dt),Y(tr_dt));
    save(['result_robbery',num2str(year(i))],'result','idx');

end