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
}