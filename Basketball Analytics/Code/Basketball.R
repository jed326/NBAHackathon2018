codes = read.table("EventCodes.txt", header = T, sep = "\t")
games = read.table("GameDataSample.txt", header = T, sep = "\t")
plays = read.table("PlayByPlay.txt", header = T, sep = "\t")
plays = plays[order(plays[,4], -plays[,6], plays[,5], plays[,2]),]
plays = plays[,-9] # remove option2
plays = plays[,-9] # remove option3

games = levels(plays$Game_id)
dfGames = list()

for(game in 1:length(games)){
  dfGames[[games[game]]] = data.frame()
}

dfNames = names(sapply(dfGames, names))
for(i in 1:dim(plays)[1]){
    dfGames[[plays$Game_id[i]]] = rbind(dfGames[[plays$Game_id[i]]], plays[i,])
  print(i)
}

for(j in 1:length(dfGames)){
  write.csv(dfGames[[j]], paste0(dfNames[j],".csv"))
}

trueTeam_ID = rep(NA, 22808)
for(i in 1:dim(plays)[1]){
  findIndex = which(as.character(plays$Person1[i]) == teamDict$Person_id)[1]
  if(length(findIndex) > 0){
    trueTeam_ID[i] = as.character(plays$Team_id[i])
  }
  else{
    trueTeam_ID[i] = as.character(teamDict$Team_id[findIndex])
  }
  print(paste0(i,"index", trueTeam_ID[i]))
}

for(i in 1:dim(plays)[1]){
  if(as.character(plays$Team_id[i]) != as.character(plays$trueTeam[i])){
    print(i)
  }
}

oneGameMerged = inner_join(oneGame, codes, by = c("Event_Msg_Type", "Action_Type"))

oneGameOrdered = oneGame[order(oneGame[,5], -oneGame[,7], oneGame[,6], oneGame[,3]),]
