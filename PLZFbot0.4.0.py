from webex_bot.models.command import Command
import logging

log = logging.getLogger(__name__)


class findplz(Command):

    def __init__(self):
        super().__init__(
            command_keyword="plz",
            help_message="Finde die zugehörige PLZ oder den Ort",
            card=None,
        )
    def execute(self, message, attachment_actions, activity):
        
        plz = input("Suche nach PLZ/Ort/Ortsteil: \n")
        with open(r'res_plz\PLZ_2021.plzf', 'r') as fp:
            # auslesen der Daten als Liste
            lines = fp.readlines()
            for line in lines:
                # suche nach plz in den Linien
                if line.find(plz) != -1:
                    print('LDN:', lines.index(line))
                    result = ('PLZ_Ort_OT ##### ', line, '\n')
        response_message = result
        return response_message

    
