from dragonfly import Function

from caster.lib import navigation, control
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class Numbers(MergeRule):
    mapping = {
            "word number <wn>":     R(Function(navigation.word_number, extra="wn"), rdescript="Number As Word"),
            "numb <wnKK>":          R(Function(navigation.numbers2, extra="wnKK"), rspec="number", rdescript="Number"),
                     
            
          }


    extras = [
        IntegerRefST("wn", 0, 10),
        IntegerRefST("wnKK", 0, 1000000),
    ]
    defaults = {}
    
control.nexus().merger.add_global_rule(Numbers())