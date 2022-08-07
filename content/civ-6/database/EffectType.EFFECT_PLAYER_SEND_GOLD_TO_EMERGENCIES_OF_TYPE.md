---
tags:
- EffectType
title: EFFECT_PLAYER_SEND_GOLD_TO_EMERGENCIES_OF_TYPE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_PLAYER_SEND_GOLD_TO_EMERGENCIES_OF_TYPE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* EmergencyType `String`
>		* [Emergencies.EmergencyType]

## Samples
```SQL {title="PROJECT_COMPLETION_SEND_AID_TO_AID_REQUESTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		Permanent
	)
VALUES
	(
		"PROJECT_COMPLETION_SEND_AID_TO_AID_REQUESTS",
		"MODIFIER_PLAYER_SEND_GOLD_TO_EMERGENCIES_OF_TYPE",
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
		"PROJECT_COMPLETION_SEND_AID_TO_AID_REQUESTS",
		"Amount",
		200
	),
	(
		"PROJECT_COMPLETION_SEND_AID_TO_AID_REQUESTS",
		"EmergencyType",
		"EMERGENCY_SEND_AID"
	);
	
```

