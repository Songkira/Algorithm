players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]


def solution(players, callings):

# 1번 방법
## 일반적인 배열로 정리하면 시간초과 뜸(최대50000건 까지 있기 때문에)
    # for i in range(len(call_lst)):
    #     for j in range(1, len(p_lst)):
    #         if call_lst[i] == p_lst[j]:
    #             p_lst[j - 1], p_lst[j] = p_lst[j], p_lst[j - 1]
    #             break

# 2번 방법
#     for i in range(len(call_lst)):
#         name = call_lst[i]
#         search_name = players.index(name)
#         # call_lst.insert(0, search_name)
#         players.insert(0, players.pop(search_name))
#
#     return p_lst

# ['mumu', 'mine', 'kai', 'soe', 'poe']

# 3번 방법(chat)
    players_dict = {player: rank for rank, player in enumerate(players, start=1)}

    for calling in callings:
        # 추월이 발생한 경우
        print(calling, "calling")
        if calling in players_dict:
            current_rank = players_dict[calling]
            print(current_rank, "current_rank")
            #이전 등수의 선수와 위치를 바꿈
            prev_player = players[current_rank - 2]
            print(prev_player, "prev")
            players_dict[calling] = current_rank - 1
            print(players_dict[calling], "players_dict[calling]")
            players_dict[prev_player] = current_rank

            print(players_dict, "dict")
            print("-------------------------------------")
    # 등수 기준으로 정렬
    # sorted_players = sorted(players_dict, key=lambda  x: players_dict[x])

    sorted_players = []
    for rank in range(1, len(players) + 1):
        for player, player_rank in players_dict.items():
            if player_rank == rank:
                sorted_players.append(player)
                break

    return sorted_players

print(solution(players, callings))