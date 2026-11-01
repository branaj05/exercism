namespace targets {
// TODO: Insert the code for the alien class here
class Alien {
  public:
    Alien(int x, int y) {
        x_coordinate = x; 
        y_coordinate = y;
    };

    int x_coordinate{};
    int y_coordinate{};

    int get_health(){
      return health; 
    }

    bool hit() {
      // tempted to replace this bool with the is_alive function but 
      // there's really no beneft to that
      if (health > 0){
        health -= 1;
      }
      return true;
    }

    bool is_alive(){
      return health>0;
    }

    bool teleport(int x, int y){
      x_coordinate = x;
      y_coordinate = y;
      return true; 
    }

    bool collision_detection(Alien other_alien){
      bool same_x = other_alien.x_coordinate == x_coordinate; 
      bool same_y = other_alien.y_coordinate == y_coordinate; 
      return same_x && same_y;
    }

  private:
    int health{3};
};
}  // namespace targets
