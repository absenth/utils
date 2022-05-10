function gatewayMAC {
    gatewayIP=$(route -n | grep -e '^0\.0\.0\.0' | tr -s ' ' | cut -d ' ' -f 2)

    if [[ ! -z "$gatewayIP" ]]
    then
        # Identify the gateway by its MAC (uniqueness...)
        gatewayData=($(arp -n $gatewayIP | grep -e $gatewayIP | tr -s ' '))
        if [[ "${gatewayData[1]}" == "(incomplete)" ]]
        then
            echo "test1"
        elif [[ "${gatewayData[2]}" == "--" ]]
        then
            echo "test2"
        else
            echo "${gatewayData[2]}"
        fi
    fi
}
