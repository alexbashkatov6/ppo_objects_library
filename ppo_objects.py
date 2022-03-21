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


class PpoTrainSignal(PpoObject):
    id_ = AnyDescriptor()
    indent = AnyDescriptor()
    idControlArea = AnyDescriptor()
    iObjTag = AnyDescriptor()
    routePointer = AnyDescriptor(is_required=False)
    groupRoutePointers = AnyDescriptor(is_list=True, is_required=False)
    uksps = AnyDescriptor(is_required=False)
    startUp = AnyDescriptor(is_required=False)


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


class PpoPointMachineCi(PpoObject):
    addrKi = AnyDescriptor()
    addrUi = AnyDescriptor()


class PpoTrackBSSO(PpoObject):
    addrKi = AnyDescriptor()
    addrUi = AnyDescriptor()


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
    iObjsTag = AnyDescriptor()
    evenTag = AnyDescriptor()
    oddTag = AnyDescriptor()


class PpoTrackReceiverRi(PpoObject):
    addrKI_P = AnyDescriptor()


class PpoLightSignalRi(PpoObject):
    addrKI_KO = AnyDescriptor()
    addrKI_KPS = AnyDescriptor()
    addrKI_RU = AnyDescriptor()
    addrKI_GM = AnyDescriptor()
    addrKI_KMGS = AnyDescriptor()
    addrKI_ZHZS = AnyDescriptor()
    addrKI_ZS = AnyDescriptor()
