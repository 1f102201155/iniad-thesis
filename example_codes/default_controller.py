def start_machine():
    # [AUTOIOT-FUNCTION-BEGIN start_machine]
    try:
        # step 1: 電源ボタン (E16A82C65393) -> press
        bot_power = Bot.find_by_id("E16A82C65393")
        _res = bot_power.press()
        if not _res.get("ok") or _res.get("httpStatus", 0) >= 400 or (_res.get("response") or {}).get("statusCode", 100) != 100:
        return Bot.make_error_response(1, "E16A82C65393", _res)


        # step 2: スタートボタン (E16A82C65394) -> press
        bot_start = Bot.find_by_id("E16A82C65394")
        _res = bot_start.press()
        if not _res.get("ok") or _res.get("httpStatus", 0) >= 400 or (_res.get("response") or {}).get("statusCode", 100) != 100:
        return Bot.make_error_response(1, "E16A82C65394", _res)

        return {"ok": True, "results": results}, 200
    except Exception as e:
        ...
    # [AUTOIOT-FUNCTION-END start_machine]
