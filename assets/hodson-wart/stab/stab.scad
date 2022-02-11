include <../wart_data.scad>

use <./stab_panel.scad>
dihedral_angle = atan2(stab_tip_dihedral,stab_span/2);

module stab() {
	rotate([dihedral_angle,0,0])
    stab_panel();
  rotate([-dihedral_angle,0,0])
    mirror([0,1,0]) 
      stab_panel();
}

stab();
