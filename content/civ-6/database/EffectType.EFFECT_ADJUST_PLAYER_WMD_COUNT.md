---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_WMD_COUNT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_WMD_COUNT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Type `String`

## Samples

```SQL {title="PROJECT_COMPLETION_MODIFIER_CREATE_NUCLEAR_DEVICE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"PROJECT_COMPLETION_MODIFIER_CREATE_NUCLEAR_DEVICE",
		"MODIFIER_PLAYER_CREATE_WMD",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PROJECT_COMPLETION_MODIFIER_CREATE_NUCLEAR_DEVICE",
		"Amount",
		1
	),
	(
		"PROJECT_COMPLETION_MODIFIER_CREATE_NUCLEAR_DEVICE",
		"Type",
		"WMD_NUCLEAR_DEVICE"
	);
	
```

