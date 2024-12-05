# System Design Interview: Volume 1 - Notes

___

* Feed publishing Diagram - P.49
    * User (Web browser, Mobile app), DNS, Load Balancer, Web Servers, Authentication - Rate Limiting, Notification
      Service, Post Service, Post
      Cache,Post DB, Fanout Service , Graph DB (get friend ids), User Cache (get friends data),User DB, Message Queue,
      Fanout Workers, News Feed Cache

* News feed retrieved - P.50
    * User (Web browser, Mobile app), DNS, CDN, Load Balancer, Web server(Authentication - Rate Limiting), News Feed
      Service, User Cache, User DB, Post Cache, Post DB, News Feed Cache