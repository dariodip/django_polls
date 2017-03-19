/**
 * Created by ddipa on 19/03/2017.
 */

$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var username = $("#hidden_username");
    var chatsock =
        new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + '/polls/' + username.val());

    chatsock.onmessage = function(message) {

        var chat = $("#online_users");
        users_td = message.data.split(",");

        chat.html('<li class="collection-header"><h5>Online users</h5></li>');
        for (u in users_td) {
            if (username.val() == users_td[u]) {
                var ele = $('<li class="collection-item active"></li>');
            } else {
                var ele = $('<li class="collection-item"></li>');
            }
                ele.append($('<i class="material-icons">perm_identity</i>'));
                ele.append($('<span></span>').text(users_td[u]));

                chat.append(ele)
            }


        };

    });