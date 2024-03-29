# SDN Controllers Synchronization
https://www.youtube.com/watch?v=ntr2gtFhHB8

SDN is an emerging networking architecture that significantly improves the network performance due to its centralized and programmable network management, easy reconfiguration, and on-demand resource allocation.  However, such centralized control suffers from scalability and reliability issues. Distributed SDN is proposed to balance centralized and distributed control over the network. A distributed SDN network is composed of a set of subnetworks (i.e., network domains), each managed by a physically independent SDN controller. The controllers synchronize with each other to maintain a logically centralized network view. Notwithstanding, since complete synchronization among controllers will incur in high costs specially in large networks, practical distributed SDN networks can  only  afford  partial  inter-controller  synchronizations. 

How controllers should be synchronized with each other to maximize the benefits of synchronizations is a research problem. This  project  models  the  problem  as  a  Markov  Decision  Process  (MDP)  problem  and explore Reinforcement Learning (RL) techniques to decide which controllers to synchronize under a given network synchronization status. The goal is to maximize the long-term benefits of controller synchronizations.  In particular, the RL agent learns over an scenario of interdomain routing

The environment is a descrete-event simulation of SDN controller's synchronization. 

