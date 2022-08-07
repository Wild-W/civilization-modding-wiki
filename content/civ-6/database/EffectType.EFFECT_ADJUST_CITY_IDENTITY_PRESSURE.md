---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_IDENTITY_PRESSURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_IDENTITY_PRESSURE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="NUCLEAR_EMERGENCY_TARGET_CULTURAL_IDENTITY_REWARD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"NUCLEAR_EMERGENCY_TARGET_CULTURAL_IDENTITY_REWARD",
		"MODIFIER_PLAYER_CITIES_ADJUST_IDENTITY_PRESSURE_FROM_EMERGENCIES",
		"NUCLEAR_EMERGENCY_REWARD_TARGET_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NUCLEAR_EMERGENCY_TARGET_CULTURAL_IDENTITY_REWARD",
		"Amount",
		"-1"
	);
	
```

