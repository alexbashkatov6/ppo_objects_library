from descriptors import AnyDescriptor


class PpoObject:
    class_ = AnyDescriptor()
    tag = AnyDescriptor()
    data = AnyDescriptor()
    to_json = AnyDescriptor()
    all_attributes = AnyDescriptor()

    def __init__(self, tag: str = ""):
        self.tag = tag


class PpoRoutePointer(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    routePointer = AnyDescriptor()


class PpoRoutePointerRi(PpoObject):
    onRoutePointer = AnyDescriptor()
    outputAddrs = AnyDescriptor()


class StartWarningArea:
    obj = AnyDescriptor()
    point = AnyDescriptor(is_required=False)


class PpoTrainSignal(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    routePointer = AnyDescriptor(is_required=False)
    groupRoutePointers = AnyDescriptor(is_list=True, is_required=False)
    uksps = AnyDescriptor(is_required=False)
    startUp = AnyDescriptor(is_required=False)
    startWarningArea = AnyDescriptor(internal_obj_type="StartWarningArea", is_required=False)


class PpoRepeatSignal(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    signalTag = AnyDescriptor()


class PpoShuntingSignal(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()


class PpoShuntingSignalWithTrackAnD(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    routePullTrain = AnyDescriptor()


class PpoLightSignalCi(PpoObject):
    mode = AnyDescriptor()
    addrKa = AnyDescriptor()
    addrKi = AnyDescriptor()
    addrUi = AnyDescriptor()
    type_ = AnyDescriptor()


class PpoAnDtrack(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    length = AnyDescriptor(default_value="5")
    trackUnit = AnyDescriptor()


class PpoTrackAnDwithPoint(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    length = AnyDescriptor(default_value="5")
    trackUnit = AnyDescriptor()
    directionPointAnDTrack = AnyDescriptor()
    oppositeTrackAnDwithPoint = AnyDescriptor()


class PpoLineEnd(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    length = AnyDescriptor(default_value="5")
    trackUnit = AnyDescriptor(default_value="nullptr")


class PpoPointSection(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    length = AnyDescriptor(default_value="5")
    trackUnit = AnyDescriptor()
    type_ = AnyDescriptor(is_required=False)


class PpoTrackSection(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    length = AnyDescriptor(default_value="5")
    trackUnit = AnyDescriptor()


class AdditionalSwitch(PpoObject):
    point = AnyDescriptor()
    selfPosition = AnyDescriptor()
    dependencePosition = AnyDescriptor()


class SectionAndIgnoreCondition(PpoObject):
    section = AnyDescriptor()
    point = AnyDescriptor(is_required=False)
    position = AnyDescriptor(is_required=False)


class NotificationPoint(PpoObject):
    point = AnyDescriptor()
    delay = AnyDescriptor()


class PpoPoint(PpoObject):
    id_ = AnyDescriptor()
    type_ = AnyDescriptor(is_required=False)
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    pointsMonitoring = AnyDescriptor()
    section = AnyDescriptor()
    railFittersWarningArea = AnyDescriptor(is_required=False)
    autoReturn = AnyDescriptor(is_required=False)
    guardPlusPlus = AnyDescriptor(is_list=True, is_required=False)
    guardPlusMinus = AnyDescriptor(is_list=True, is_required=False)
    guardMinusPlus = AnyDescriptor(is_list=True, is_required=False)
    guardMinusMinus = AnyDescriptor(is_list=True, is_required=False)
    lockingPlus = AnyDescriptor(is_list=True, is_required=False)
    lockingMinus = AnyDescriptor(is_list=True, is_required=False)
    additionalSwitch = AnyDescriptor(internal_obj_type="AdditionalSwitch", is_list=True, is_required=False)
    pairPoint = AnyDescriptor(is_required=False)
    oversizedPlus = AnyDescriptor(internal_obj_type="SectionAndIgnoreCondition", is_list=True, is_required=False)
    oversizedMinus = AnyDescriptor(internal_obj_type="SectionAndIgnoreCondition", is_list=True, is_required=False)
    additionalGuardLock = AnyDescriptor(internal_obj_type="SectionAndIgnoreCondition", is_list=True, is_required=False)
    lockingPlusSignal = AnyDescriptor(is_list=True, is_required=False)
    lockingMinusSignal = AnyDescriptor(is_list=True, is_required=False)


class PpoPointMachineCi(PpoObject):
    addrKi = AnyDescriptor()
    addrUi = AnyDescriptor()


class PpoAxisCountingCi(PpoObject):
    receiverAddr = AnyDescriptor()


class PpoGroupRailFittersWarningArea(PpoObject):
    pass


class PpoRailFittersWarningAreaRi(PpoObject):
    AddrMKI_KNM = AnyDescriptor()
    AddrMUI_RRM = AnyDescriptor()
    AddrMUI_OM = AnyDescriptor()


class PpoRailFittersWarningArea(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    group = AnyDescriptor()
    points = AnyDescriptor(is_list=True)


class PpoCabinetUsoBk(PpoObject):
    lightSignals = AnyDescriptor(is_list=True)
    hiCratePointMachines = AnyDescriptor(is_list=True)
    loCratePointMachines = AnyDescriptor(is_list=True)
    controlDeviceDerailmentStocks = AnyDescriptor(is_list=True)


class PpoInsulationResistanceMonitoring(PpoObject):
    cabinets = AnyDescriptor(is_list=True)
    addrKI_OK = AnyDescriptor()


class PpoPointMachinesCurrentMonitoring(PpoObject):
    cabinets = AnyDescriptor(is_list=True)
    addrKI_KTPS = AnyDescriptor()


class PpoTelesignalization(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()


class PpoPointsMonitoring(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()


class PpoLightModeRi(PpoObject):
    addrKI_DN1 = AnyDescriptor()
    addrKI_DN2 = AnyDescriptor()
    addrKI_DSN = AnyDescriptor()
    addrUI_DN = AnyDescriptor()
    addrUI_DSN = AnyDescriptor()
    addrUI_ASV = AnyDescriptor()


class PpoLightMode(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()


class PpoFireAndSecurityAlarm(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()


class PpoDieselGenerator(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    dieselControl = AnyDescriptor()
    startDieselGenerator = AnyDescriptor()
    stopDieselGenerator = AnyDescriptor()


class PpoGeneralPurposeRelayInput(PpoObject):
    inputAddr = AnyDescriptor(is_list=True)


class PpoGeneralPurposeRelayOutput(PpoObject):
    addrUI = AnyDescriptor()
    defaultValue = AnyDescriptor(is_required=False)


class PpoControlAreaBorder(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()


class PpoSemiAutomaticBlockingSystem(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    isInvitationSignalOpeningBefore = AnyDescriptor()


class PpoSemiAutomaticBlockingSystemRi(PpoObject):
    addrKI_SNP = AnyDescriptor()
    addrKI_S1U = AnyDescriptor()
    addrKI_1U = AnyDescriptor()
    addrKI_FP = AnyDescriptor()
    addrKI_POS = AnyDescriptor()
    addrKI_PS = AnyDescriptor()
    addrKI_OP = AnyDescriptor()
    addrKI_DSO = AnyDescriptor()
    addrKI_KZH = AnyDescriptor()

    addrUI_KS = AnyDescriptor()

    output_DSO = AnyDescriptor()
    output_OSO = AnyDescriptor()
    output_FDP = AnyDescriptor()
    output_IFP = AnyDescriptor()

    notificationPoints = AnyDescriptor(internal_obj_type="NotificationPoint", is_list=True)


class PpoAutomaticBlockingSystem(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    isInvitationSignalOpeningBefore = AnyDescriptor()
    singleTrack = AnyDescriptor()


class PpoAutomaticBlockingSystemRi(PpoObject):
    addrKI_SNP = AnyDescriptor()
    addrKI_SN = AnyDescriptor()
    addrKI_S1U = AnyDescriptor()
    addrKI_S1P = AnyDescriptor()
    addrKI_1U = AnyDescriptor()
    addrKI_1P = AnyDescriptor()
    addrKI_2U = AnyDescriptor()
    addrKI_3U = AnyDescriptor()
    addrKI_ZU = AnyDescriptor()
    addrKI_KP = AnyDescriptor()
    addrKI_KZH = AnyDescriptor()
    addrKI_UUB = AnyDescriptor()
    addrKI_PB = AnyDescriptor()
    addrKI_KV = AnyDescriptor()
    addrKI_A = AnyDescriptor()

    addrUI_KS = AnyDescriptor()
    addrUI_I = AnyDescriptor()
    addrUI_KZH = AnyDescriptor()
    addrUI_VIP1 = AnyDescriptor()
    addrUI_VIP2 = AnyDescriptor()
    addrUI_VIP3 = AnyDescriptor()
    addrUI_OKV = AnyDescriptor()
    addrUI_KM = AnyDescriptor()

    output_SNK = AnyDescriptor()
    output_DS = AnyDescriptor()
    output_OV = AnyDescriptor()
    output_PV = AnyDescriptor()
    output_RUU = AnyDescriptor()
    output_R = AnyDescriptor()

    adjEnterSig = AnyDescriptor()

    notificationPoints = AnyDescriptor(internal_obj_type="NotificationPoint", is_list=True)


class PpoTrackCrossroad(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    railCrossing = AnyDescriptor()


class PpoTrainNotificationRi(PpoObject):
    NPI = AnyDescriptor()
    CHPI = AnyDescriptor()


class PpoRailCrossingRi(PpoObject):
    NCHPI = AnyDescriptor()
    KP_O = AnyDescriptor()
    KP_A = AnyDescriptor()
    ZG = AnyDescriptor()
    KZP = AnyDescriptor()


class PpoRailCrossing(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    crossroad = AnyDescriptor(is_list=True)


class PpoControlDeviceDerailmentStock(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()


class PpoControlDeviceDerailmentStockCi(PpoObject):
    addrKI_1KSO = AnyDescriptor()
    addrKI_1KSR = AnyDescriptor()
    addrKI_2KSO = AnyDescriptor()
    addrKI_2KSR = AnyDescriptor()

    addrKI_KSV = AnyDescriptor()
    addrKI_SNP = AnyDescriptor()
    addrKI_1UP = AnyDescriptor()
    addrKI_2UP = AnyDescriptor()
    addrKI_1UU = AnyDescriptor()
    addrKI_2UU = AnyDescriptor()

    addrUI_1KSD = AnyDescriptor()
    addrUI_2KSB = AnyDescriptor()
    addrUI_KSVA = AnyDescriptor()

    enterSignal = AnyDescriptor()


class PpoTrackUnit(PpoObject):
    iObjsTag = AnyDescriptor(is_list=True)
    evenTag = AnyDescriptor(is_required=False)
    oddTag = AnyDescriptor(is_required=False)


class PpoTrackReceiverRi(PpoObject):
    addrKI_P = AnyDescriptor()


class PpoLightSignalRi(PpoObject):
    addrKI_KO = AnyDescriptor(default_value="USO:0")
    addrKI_KPS = AnyDescriptor(default_value="USO:MAX_UINT")
    addrKI_S = AnyDescriptor(default_value="USO:MAX_UINT")
    addrKI_RU = AnyDescriptor(default_value="USO:MAX_UINT")
    addrKI_GM = AnyDescriptor(default_value="USO:MAX_UINT")
    addrKI_KMGS = AnyDescriptor(default_value="USO:MAX_UINT")
    addrKI_ZHZS = AnyDescriptor(default_value="USO:MAX_UINT")
    addrKI_ZS = AnyDescriptor(default_value="USO:MAX_UINT")
    # addrKI_KO = AnyDescriptor(default_value="Fixed_0")
    # addrKI_KPS = AnyDescriptor(default_value="Fixed_0")
    # addrKI_S = AnyDescriptor(default_value="Fixed_0")
    # addrKI_RU = AnyDescriptor(default_value="Fixed_0")
    # addrKI_GM = AnyDescriptor(default_value="Fixed_0")
    # addrKI_KMGS = AnyDescriptor(default_value="Fixed_0")
    # addrKI_ZHZS = AnyDescriptor(default_value="Fixed_0")
    # addrKI_ZS = AnyDescriptor(default_value="Fixed_0")


class PpoElectropneumaticValveRi(PpoObject):
    addrKI_KEPK = AnyDescriptor(default_value="Fixed_1")
    addrUI_OEPK = AnyDescriptor(default_value="NoAddr")
    addrUI_VS1 = AnyDescriptor(default_value="NoAddr")
    addrUI_VS2 = AnyDescriptor(default_value="NoAddr")
    addrUI_VS3 = AnyDescriptor(default_value="NoAddr")
    addrUI_VS4 = AnyDescriptor(default_value="NoAddr")
    addrUI_VS5 = AnyDescriptor(default_value="NoAddr")
    addrUI_VS6 = AnyDescriptor(default_value="NoAddr")
    addrUI_VS7 = AnyDescriptor(default_value="NoAddr")
    addrUI_VS8 = AnyDescriptor(default_value="NoAddr")


class PpoPneumaticCleaningCompressorRi(PpoObject):
    addrKI_RD = AnyDescriptor(default_value="Fixed_1")
    addrUI_OSV = AnyDescriptor(default_value="NoAddr")
    output_RDP = AnyDescriptor(default_value="RDP")
    output_RDO = AnyDescriptor(default_value="RDO")


class PpoPneumaticCleaningValve(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    point = AnyDescriptor()


class PpoPneumaticCleaningArea(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    valves = AnyDescriptor(is_list=True)
