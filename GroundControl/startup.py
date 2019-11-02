#!/usr/bin/env python3

import argparse
import logging


logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)

logging.info('Starting Ground Control')
