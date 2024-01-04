export interface DisplayInfoItem {
    "username":string;
    "name":string;
    "email":string;
}

export interface SetStateButtonOptions {
    setState: () => void
    stateInfo: any
}

export interface SetStateDisplayOptions {
    stateInfo: any
    stateName: string;
}

export interface DisplayProps {
    openArea: boolean;
    openInfo: boolean
    userInfo: DisplayInfoItem[] | [];
}
