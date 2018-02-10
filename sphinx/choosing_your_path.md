# Choosing Your Path

Your party will be faced with either one or two doors when you complete a room. If there is one, the only way you can go is forward by returning (```Direction.forward```) in the (```room_choice```) method. If there are two, you can go left or right by returning (```Direction.left```) or (```Direction.Right```). In this method you can also get the room object from (```options[Direction.right]```) or (```options[Direction.left]```) in order to look at its properties. Before you look at the properties you will first want to determine what kind of room it is, to do this you can check the following, (```room.node_type == NodeType.town```), (```room.node_type == NodeType.monster```), (```room.node_type == NodeType.trap```). If the room is a monster room you can do (```room.```) any of the properties found in [Monster Properties](~documentation/overview.html#choosing-your-path) and same for traps but using the properties found in [Trap Properties](~documentation/traps.html#trap-properties).