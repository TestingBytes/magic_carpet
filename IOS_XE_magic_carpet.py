# ----------------
# Copywrite
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco

# ----------------
# Python
# ----------------
import os
import sys
import yaml
import time
import json
import shutil
import logging
from pyats import aetest

# ----------------
# Jinja2
# ----------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'templates/cisco/ios_xe'
env = Environment(loader=FileSystemLoader(template_dir))

# ----------------
# Import pyATS and the pyATS Library
# ----------------
from pyats import topology
from pyats.log.utils import banner

# Get logger for script
log = logging.getLogger(__name__)

# ----------------
# Template sources
# ----------------

# ip int brief
sh_ip_int_brief_csv_template = env.get_template('show_ip_int_brief_csv.j2')
sh_ip_int_brief_md_template = env.get_template('show_ip_int_brief_md.j2')
sh_ip_int_brief_html_template = env.get_template('show_ip_int_brief_html.j2')

# int status
sh_int_status_csv_template = env.get_template('show_int_status_csv.j2')
sh_int_status_md_template = env.get_template('show_int_status_md.j2')
sh_int_status_html_template = env.get_template('show_int_status_html.j2')

# version
sh_ver_csv_template = env.get_template('show_version_csv.j2')
sh_ver_md_template = env.get_template('show_version_md.j2')
sh_ver_html_template = env.get_template('show_version_html.j2')

# inventory

# 4500
sh_inventory_4500_csv_template = env.get_template('show_inventory_4500_csv.j2')
sh_inventory_4500_md_template = env.get_template('show_inventory_4500_md.j2')
sh_inventory_4500_html_template = env.get_template('show_inventory_4500_html.j2')

# 3850
sh_inventory_3850_csv_template = env.get_template('show_inventory_3850_csv.j2')
sh_inventory_3850_md_template = env.get_template('show_inventory_3850_md.j2')
sh_inventory_3850_html_template = env.get_template('show_inventory_3850_html.j2')

# 9300
sh_inventory_9300_csv_template = env.get_template('show_inventory_9300_csv.j2')
sh_inventory_9300_md_template = env.get_template('show_inventory_9300_md.j2')
sh_inventory_9300_html_template = env.get_template('show_inventory_9300_html.j2')

# ip access-lists
sh_access_lists_csv_template = env.get_template('show_access_lists_csv.j2')
sh_access_lists_md_template = env.get_template('show_access_lists_md.j2')
sh_access_lists_html_template = env.get_template('show_access_lists_html.j2')

# show ntp associations
sh_ntp_associations_csv_template = env.get_template('show_ntp_associations_csv.j2')
sh_ntp_associations_md_template = env.get_template('show_ntp_associations_md.j2')
sh_ntp_associations_html_template = env.get_template('show_ntp_associations_html.j2')

# vrf
sh_vrf_csv_template = env.get_template('show_vrf_csv.j2')
sh_vrf_md_template = env.get_template('show_vrf_md.j2')
sh_vrf_html_template = env.get_template('show_vrf_html.j2')

# IP ARP
sh_ip_arp_csv_template = env.get_template('show_ip_arp_csv.j2')
sh_ip_arp_md_template = env.get_template('show_ip_arp_md.j2')
sh_ip_arp_html_template = env.get_template('show_ip_arp_html.j2')

# IP ARP VRF <VRF>
sh_ip_arp_vrf_csv_template = env.get_template('show_ip_arp_csv.j2')
sh_ip_arp_vrf_md_template = env.get_template('show_ip_arp_md.j2')
sh_ip_arp_vrf_html_template = env.get_template('show_ip_arp_html.j2')

class common_setup(aetest.CommonSetup):
    """Common Setup section"""
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        log.info(banner("Hang on tight - we are about to go on a magic carpet ride!\n.-.\n[.-''-.,\n|  //`~\)\n(<|0|>0)\n;\  _/ \\_ _\,\n__\|'._/_  \ '='-,\n/\ \    || )_///_\>>\n(  '._ T |\ | _/),-'\n'.   '._.-' /'/ |\n| '._   _.'`-.._/\n,\ / '-' |/\n[_/\-----j\n_.--.__[_.--'_\__\n/         `--'    '---._\n/ '---.  -'. .'  _.--   '.\n\_      '--.___ _;.-o     /\n'.__ ___/______.__8----'\nc-'----'\n\n\n###___Loading testbed___###"))
        testbed.connect()

# Testcase name : tc_one
class Collect_Information(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def parse(self, testbed, section, steps):
        """ Testcase Setup section """
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        for device in testbed:
            # ---------------------------------------
            # Execute parser to show interface status
            # ---------------------------------------
            log.info(banner("_.---.__\n.'        `-.\n/      .--.   |\n\/  / /    |_/\n`\/|/    _(_)\n___  /|_.--'    `.   .\n\  `--' .---.     \ /|\n)   `       \     //|\n| __    __   |   '/||\n|/  \  /  \      / ||\n||  |  |   \     \  |\n\|  |  |   /        |\n__\\@/  |@ | ___ \--'\n(     /' `--'  __)|\n__>   (  .  .--' & \n/   `--|_/--'     &  |\n|                 #. |\n|                 q# |\n\              ,ad#'\n`.________.ad####'\n`#####''''''\n`&#\n&# #&\n'#ba'\n'\n\nThe Magic Carpet is heading into the Code of Wonders\nGenie Parsing Has Begun"))

            with steps.start('Parsing show ip interface brief',continue_=True) as step:
                try:
                    self.parsed_show_ip_int_brief = device.parse("show ip interface brief")
                except Exception as e:
                    step.failed('Could not parse it correctly\n{e}'.format(e=e))

            with steps.start('Parsing show ip interfaces status',continue_=True) as step:
                try:
                    self.parsed_show_int_status = device.parse("show interfaces status")
                except Exception as e:
                    step.failed('Could not parse it correctly\n{e}'.format(e=e))

            with steps.start('Parsing show version',continue_=True) as step:
                try:
                    self.parsed_show_version = device.parse("show version")
                except Exception as e:
                    step.failed('Could not parse it correctly\n{e}'.format(e=e))

            with steps.start('Parsing show inventory',continue_=True) as step:
                try:
                    self.parsed_show_inventory = device.parse("show inventory")
                except Exception as e:
                    step.failed('Could not parse it correctly\n{e}'.format(e=e))

            with steps.start('Parsing show ntp associations',continue_=True) as step:
                try:
                    self.parsed_show_ntp_associations = device.parse("show ntp associations")
                except Exception as e:
                    step.failed('Could not parse it correctly\n{e}'.format(e=e))

            with steps.start('Parsing show access-lists',continue_=True) as step:
                try:
                    self.parsed_show_access_lists = device.parse("show access-lists")
                except Exception as e:
                    step.failed('Could not parse it correctly\n{e}'.format(e=e))

            with steps.start('Parsing show vrf',continue_=True) as step:
                try:
                    self.parsed_show_vrf = device.parse("show vrf")
                except Exception as e:
                    step.failed('Could not parse it correctly\n{e}'.format(e=e))

            with steps.start('Parsing ip arp',continue_=True) as step:
                try:
                    self.parsed_show_ip_arp = device.parse("show ip arp")
                except Exception as e:
                    step.failed('Could not parse it correctly\n{e}'.format(e=e))

            with steps.start('Store data',continue_=True) as step:

                # Show ip int brief
                if hasattr(self, 'parsed_show_ip_int_brief'):
                    output_from_parsed_ip_int_brief_csv_template = sh_ip_int_brief_csv_template.render(to_parse_interfaces=self.parsed_show_ip_int_brief['interface'])
                    output_from_parsed_ip_int_brief_md_template = sh_ip_int_brief_md_template.render(to_parse_interfaces=self.parsed_show_ip_int_brief['interface'])
                    output_from_parsed_ip_int_brief_html_template = sh_ip_int_brief_html_template.render(to_parse_interfaces=self.parsed_show_ip_int_brief['interface'])

                # Show int status
                if hasattr(self, 'parsed_show_int_status'):
                    output_from_parsed_int_status_csv_template = sh_int_status_csv_template.render(to_parse_interfaces=self.parsed_show_int_status['interfaces'])
                    output_from_parsed_int_status_md_template = sh_int_status_md_template.render(to_parse_interfaces=self.parsed_show_int_status['interfaces'])
                    output_from_parsed_int_status_html_template = sh_int_status_html_template.render(to_parse_interfaces=self.parsed_show_int_status['interfaces'])

                # Show version
                if hasattr(self, 'parsed_show_version'):
                    output_from_parsed_version_csv_template = sh_ver_csv_template.render(to_parse_version=self.parsed_show_version['version'])
                    output_from_parsed_version_md_template = sh_ver_md_template.render(to_parse_version=self.parsed_show_version['version'])
                    output_from_parsed_version_html_template = sh_ver_html_template.render(to_parse_version=self.parsed_show_version['version'])

                # Show inventory
                if hasattr(self, 'parsed_show_inventory'):

                    # 4500
                    if device.platform == "cat4500":
                      output_from_parsed_inventory_4500_csv_template = sh_inventory_4500_csv_template.render(to_parse_inventory=self.parsed_show_inventory['main'])
                      output_from_parsed_inventory_4500_md_template = sh_inventory_4500_md_template.render(to_parse_inventory=self.parsed_show_inventory['main'])
                      output_from_parsed_inventory_4500_html_template = sh_inventory_4500_html_template.render(to_parse_inventory=self.parsed_show_inventory['main'])

                    # 3850
                    elif device.platform == "cat3850":
                      output_from_parsed_inventory_3850_csv_template = sh_inventory_3850_csv_template.render(to_parse_inventory=self.parsed_show_inventory['slot'])
                      output_from_parsed_inventory_3850_md_template = sh_inventory_3850_md_template.render(to_parse_inventory=self.parsed_show_inventory['slot'])
                      output_from_parsed_inventory_3850_html_template = sh_inventory_3850_html_template.render(to_parse_inventory=self.parsed_show_inventory['slot'])

                    # 9300
                    elif device.platform == "cat9300":
                      output_from_parsed_inventory_9300_csv_template = sh_inventory_9300_csv_template.render(to_parse_inventory=self.parsed_show_inventory['slot'])
                      output_from_parsed_inventory_9300_md_template = sh_inventory_9300_md_template.render(to_parse_inventory=self.parsed_show_inventory['slot'])
                      output_from_parsed_inventory_9300_html_template = sh_inventory_9300_html_template.render(to_parse_inventory=self.parsed_show_inventory['slot'])

                # Show access-lists
                if hasattr(self, 'parsed_show_access_lists'):
                    output_from_parsed_access_lists_csv_template = sh_access_lists_csv_template.render(to_parse_access_list=self.parsed_show_access_lists)
                    output_from_parsed_access_lists_md_template = sh_access_lists_md_template.render(to_parse_access_list=self.parsed_show_access_lists)
                    output_from_parsed_access_lists_html_template = sh_access_lists_html_template.render(to_parse_access_list=self.parsed_show_access_lists)

                # Show ntp associations
                if hasattr(self, 'parsed_show_ntp_associations'):
                    output_from_parsed_ntp_associations_csv_template = sh_ntp_associations_csv_template.render(to_parse_ntp_associations=self.parsed_show_ntp_associations)
                    output_from_parsed_ntp_associations_md_template = sh_ntp_associations_md_template.render(to_parse_ntp_associations=self.parsed_show_ntp_associations)
                    output_from_parsed_ntp_associations_html_template = sh_ntp_associations_html_template.render(to_parse_ntp_associations=self.parsed_show_ntp_associations)

                # Show vrf
                if hasattr(self, 'parsed_show_vrf'):
                    output_from_parsed_vrf_csv_template = sh_vrf_csv_template.render(to_parse_vrf=self.parsed_show_vrf['vrf'])
                    output_from_parsed_vrf_md_template = sh_vrf_md_template.render(to_parse_vrf=self.parsed_show_vrf['vrf'])
                    output_from_parsed_vrf_html_template = sh_vrf_html_template.render(to_parse_vrf=self.parsed_show_vrf['vrf'])

                # Show ip arp
                if hasattr(self, 'parsed_show_ip_arp'):
                    output_from_parsed_ip_arp_csv_template = sh_ip_arp_csv_template.render(to_parse_ip_arp=self.parsed_show_ip_arp['interfaces'])
                    output_from_parsed_ip_arp_md_template = sh_ip_arp_md_template.render(to_parse_ip_arp=self.parsed_show_ip_arp['interfaces'])
                    output_from_parsed_ip_arp_html_template = sh_ip_arp_html_template.render(to_parse_ip_arp=self.parsed_show_ip_arp['interfaces'])

                # ---------------------------------------
                # Create Files
                # ---------------------------------------

                # Show IP Interface Brief
                if hasattr(self, 'parsed_show_ip_int_brief'):
                    with open("Cave_of_Wonders/Show_IP_Interface_Brief/%s_show_ip_int_brief.json" % device.alias, "w") as fid:
                      json.dump(self.parsed_show_ip_int_brief, fid, indent=4, sort_keys=True)

                    with open("Cave_of_Wonders/Show_IP_Interface_Brief/%s_show_ip_int_brief.yaml" % device.alias, "w") as yml:
                      yaml.dump(self.parsed_show_ip_int_brief, yml, allow_unicode=True)

                    with open("Cave_of_Wonders/Show_IP_Interface_Brief/%s_show_ip_int_brief.csv" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_ip_int_brief_csv_template)

                    with open("Cave_of_Wonders/Show_IP_Interface_Brief/%s_show_ip_int_brief.md" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_ip_int_brief_md_template)

                    with open("Cave_of_Wonders/Show_IP_Interface_Brief/%s_show_ip_int_brief.html" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_ip_int_brief_html_template)

                # Show Interfaces Status
                if hasattr(self, 'parsed_show_int_status'):
                    with open("Cave_of_Wonders/Show_Interfaces_Status/%s_show_int_status.json" % device.alias, "w") as fid:
                      json.dump(self.parsed_show_int_status, fid, indent=4, sort_keys=True)

                    with open("Cave_of_Wonders/Show_Interfaces_Status/%s_show_int_status.yaml" % device.alias, "w") as yml:
                      yaml.dump(self.parsed_show_int_status, yml, allow_unicode=True)

                    with open("Cave_of_Wonders/Show_Interfaces_Status/%s_show_int_status.csv" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_int_status_csv_template)

                    with open("Cave_of_Wonders/Show_Interfaces_Status/%s_show_int_status.md" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_int_status_md_template)

                    with open("Cave_of_Wonders/Show_Interfaces_Status/%s_show_int_status.html" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_int_status_html_template)

                # Show Version
                if hasattr(self, 'parsed_show_version'):
                    with open("Cave_of_Wonders/Show_Version/%s_show_version.json" % device.alias, "w") as fid:
                      json.dump(self.parsed_show_version, fid, indent=4, sort_keys=True)

                    with open("Cave_of_Wonders/Show_Version/%s_show_version.yaml" % device.alias, "w") as yml:
                      yaml.dump(self.parsed_show_version, yml, allow_unicode=True)

                    with open("Cave_of_Wonders/Show_Version/%s_show_version.csv" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_version_csv_template)

                    with open("Cave_of_Wonders/Show_Version/%s_show_version.md" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_version_md_template)

                    with open("Cave_of_Wonders/Show_Version/%s_show_version.html" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_version_html_template)

                # Show Inventory
                if hasattr(self, 'parsed_show_inventory'):
                    with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.json" % device.alias, "w") as fid:
                      json.dump(self.parsed_show_inventory, fid, indent=4, sort_keys=True)

                    with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.yaml" % device.alias, "w") as yml:
                      yaml.dump(self.parsed_show_inventory, yml, allow_unicode=True)

                    # 4500
                    if device.platform == "cat4500":
                      with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.csv" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_inventory_4500_csv_template)

                      with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.md" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_inventory_4500_md_template)

                      with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.html" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_inventory_4500_html_template)

                    # 3850
                    elif device.platform == "cat3850":
                      with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.csv" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_inventory_3850_csv_template)

                      with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.md" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_inventory_3850_md_template)

                      with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.html" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_inventory_3850_html_template)

                    # 9300
                    elif device.platform == "cat9300":
                      with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.csv" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_inventory_9300_csv_template)

                      with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.md" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_inventory_9300_md_template)

                      with open("Cave_of_Wonders/Show_Inventory/%s_show_inventory.html" % device.alias, "w") as fh:
                        fh.write(output_from_parsed_inventory_9300_html_template)

                # Show Access-Lists
                if hasattr(self, 'parsed_show_access_lists'):
                    with open("Cave_of_Wonders/Show_Access_Lists/%s_show_access_lists.json" % device.alias, "w") as fid:
                      json.dump(self.parsed_show_access_lists, fid, indent=4, sort_keys=True)

                    with open("Cave_of_Wonders/Show_Access_Lists/%s_show_access_lists.yaml" % device.alias, "w") as yml:
                      yaml.dump(self.parsed_show_access_lists, yml, allow_unicode=True)

                    with open("Cave_of_Wonders/Show_Access_Lists/%s_show_access_lists.csv" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_access_lists_csv_template)

                    with open("Cave_of_Wonders/Show_Access_Lists/%s_show_access_lists.md" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_access_lists_md_template)

                    with open("Cave_of_Wonders/Show_Access_Lists/%s_show_access_lists.html" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_access_lists_html_template)

                # Show NTP Associations
                if hasattr(self, 'parsed_show_ntp_associations'):
                    with open("Cave_of_Wonders/Show_NTP_Associations/%s_show_ntp_associations.json" % device.alias, "w") as fid:
                      json.dump(self.parsed_show_ntp_associations, fid, indent=4, sort_keys=True)

                    with open("Cave_of_Wonders/Show_NTP_Associations/%s_show_ntp_associations.yaml" % device.alias, "w") as yml:
                      yaml.dump(self.parsed_show_ntp_associations, yml, allow_unicode=True)

                    with open("Cave_of_Wonders/Show_NTP_Associations/%s_show_ntp_associations.csv" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_ntp_associations_csv_template)

                    with open("Cave_of_Wonders/Show_NTP_Associations/%s_show_ntp_associations.md" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_ntp_associations_md_template)

                    with open("Cave_of_Wonders/Show_NTP_Associations/%s_show_ntp_associations.html" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_ntp_associations_html_template)

                # Show IP ARP
                if hasattr(self, 'parsed_show_ip_arp'):
                    with open("Cave_of_Wonders/Show_IP_ARP/%s_show_ip_arp.json" % device.alias, "w") as fid:
                      json.dump(self.parsed_show_ip_arp, fid, indent=4, sort_keys=True)

                    with open("Cave_of_Wonders/Show_IP_ARP/%s_show_ip_arp.yaml" % device.alias, "w") as yml:
                      yaml.dump(self.parsed_show_ip_arp, yml, allow_unicode=True)

                    with open("Cave_of_Wonders/Show_IP_ARP/%s_show_ip_arp.csv" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_ip_arp_csv_template)

                    with open("Cave_of_Wonders/Show_IP_ARP/%s_show_ip_arp.md" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_ip_arp_md_template)

                    with open("Cave_of_Wonders/Show_IP_ARP/%s_show_ip_arp.html" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_ip_arp_html_template)

                # Show VRF
                if hasattr(self, 'parsed_show_vrf'):
                    with open("Cave_of_Wonders/Show_VRF/%s_show_vrf.json" % device.alias, "w") as fid:
                      json.dump(self.parsed_show_vrf, fid, indent=4, sort_keys=True)

                    with open("Cave_of_Wonders/Show_VRF/%s_show_vrf.yaml" % device.alias, "w") as yml:
                      yaml.dump(self.parsed_show_vrf, yml, allow_unicode=True)

                    with open("Cave_of_Wonders/Show_VRF/%s_show_vrf.csv" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_vrf_csv_template)

                    with open("Cave_of_Wonders/Show_VRF/%s_show_vrf.md" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_vrf_md_template)

                    with open("Cave_of_Wonders/Show_VRF/%s_show_vrf.html" % device.alias, "w") as fh:
                      fh.write(output_from_parsed_vrf_html_template)

                    # Show IP ARP VRF <VRF> 
                    for vrf in self.parsed_show_vrf['vrf']:
                        with steps.start('Parsing ip arp vrf',continue_=True) as step:
                            try:
                                self.parsed_show_ip_arp_vrf = device.parse("show ip arp vrf %s" % vrf)
                            except Exception as e:
                                step.failed('Could not parse it correctly\n{e}'.format(e=e))

                        with steps.start('Store data',continue_=True) as step:

                            # Show ip arp
                            output_from_parsed_ip_arp_vrf_csv_template = sh_ip_arp_vrf_csv_template.render(to_parse_ip_arp=self.parsed_show_ip_arp_vrf['interfaces'])
                            output_from_parsed_ip_arp_vrf_md_template = sh_ip_arp_vrf_md_template.render(to_parse_ip_arp=self.parsed_show_ip_arp_vrf['interfaces'])
                            output_from_parsed_ip_arp_vrf_html_template = sh_ip_arp_vrf_html_template.render(to_parse_ip_arp=self.parsed_show_ip_arp_vrf['interfaces'])

                            with open("Cave_of_Wonders/Show_IP_ARP_VRF/%s_show_ip_arp_vrf_%s.json" % (device.alias,vrf), "w") as fid:
                              json.dump(self.parsed_show_ip_arp_vrf, fid, indent=4, sort_keys=True)

                            with open("Cave_of_Wonders/Show_IP_ARP_VRF/%s_show_ip_arp_vrf_%s.yaml" % (device.alias,vrf), "w") as yml:
                              yaml.dump(self.parsed_show_ip_arp_vrf, yml, allow_unicode=True)

                            with open("Cave_of_Wonders/Show_IP_ARP_VRF/%s_show_ip_arp_vrf_%s.csv" % (device.alias,vrf), "w") as fh:
                              fh.write(output_from_parsed_ip_arp_vrf_csv_template)

                            with open("Cave_of_Wonders/Show_IP_ARP_VRF/%s_show_ip_arp_vrf_%s.md" % (device.alias,vrf), "w") as fh:
                              fh.write(output_from_parsed_ip_arp_vrf_md_template)

                            with open("Cave_of_Wonders/Show_IP_ARP_VRF/%s_show_ip_arp_vrf_%s.html" % (device.alias,vrf), "w") as fh:
                              fh.write(output_from_parsed_ip_arp_vrf_html_template)

        # For loop done - We're done here!
        # Copy all Wonders to runinfo so it is visible in the logviewer
        # Not working - but should work next week - This would allow to 
        # see all the Wonders in the brower too!
        # shutil.copytree('Wonders', os.path.join(self.parameters['runinfo_dir'], 'Wonders'))

        # Goodbye Banner
        log.info(banner("You've made it out of the Code of Wonders on your Magic Carpet!\nWhat treasures did you get?\n\n_oOoOoOo_\n(oOoOoOoOo)\n)`#####`(\n/         \ \n|  NETWORK  |\n|  D A T A  |\n\           /\n`=========`\n\n To see the results of your Magic Carpet ride type\n pyats logs view\n\nWritten by John Capobianco March 2021"))