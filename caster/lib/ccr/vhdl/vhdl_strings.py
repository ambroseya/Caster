
case_string=Text("case TOKEN is")+Key("enter,tab")+Text("when 'TOKEN'  =>  TOKEN")+\
Key("enter,backspace")+Text("end case;")

process_string=\
Text("TOKEN: process()")+Key("enter")+Text("begin")+\
Key("enter,tab")+Text("TOKEN")+Key("enter,backspace")+Text("end process;")

component_string=\
Text("TOKEN: TOKEN")+Key("enter")+Text("(")+\
Key("right,semicolon,left:2,enter,tab")+Text("port map(")+Key("enter,tab")+Text("TOKEN <= TOKEN,")+\
Key("right,enter,s-home,backspace")

component_declaration_string=\
Text("component TOKEN is")+Key("enter,tab")+Text("port (TOKEN: in std_logic;")+\
Key("enter")+Text(");")+Key("enter,backspace")+Text("end component;")

entity_string=Text("entity TOKEN is")+Key("enter,tab")+Text("port (TOKEN: in std_logic;")+\
Key("enter")+Text(");")+Key("enter,backspace")+Text("end entity;")

architecture_string=\
Text("architecture TOKEN is")+Key("enter")+Text("begin")+\
Key("enter,tab")+Text("TOKEN")+Key("enter,backspace")+Text("end architecture;")