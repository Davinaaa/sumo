#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to shape mode
netedit.shapeMode()

# go to shape mode
netedit.changeShape("poly")

# change angle (invalid)
netedit.modifyShapeDefaultValue(9, "dummyAngle")

# try to create polygon
netedit.createSquaredPoly(match, 100, 50, 100, True)

# change angle (valid, but > 360)
netedit.modifyShapeDefaultValue(9, "365")

# try to create polygon
netedit.createSquaredPoly(match, 200, 50, 100, True)

# change angle (valid, < 0)
netedit.modifyShapeDefaultValue(9, "-5")

# create polygon
netedit.createSquaredPoly(match, 300, 50, 100, True)

# change angle (0 < angle < 360)
netedit.modifyShapeDefaultValue(9, "5")

# create polygon
netedit.createSquaredPoly(match, 400, 50, 100, True)

# Check undo redo
netedit.undo(match, 3)
netedit.redo(match, 3)

# save shapes
netedit.saveShapes()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
