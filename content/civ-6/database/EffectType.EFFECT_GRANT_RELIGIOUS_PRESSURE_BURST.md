---
tags:
- EffectType
title: EFFECT_GRANT_RELIGIOUS_PRESSURE_BURST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_RELIGIOUS_PRESSURE_BURST
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* Range `Integer`

## Samples
```SQL {title="RELIGIOUS_EMERGENCY_TARGET_PRESSURE_REWARD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"RELIGIOUS_EMERGENCY_TARGET_PRESSURE_REWARD",
		"MODIFIER_EMERGENCY_CITIES_EXERT_RELIGIOUS_PRESSURE",
		"RELIGIOUS_EMERGENCY_REWARD_TARGET_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RELIGIOUS_EMERGENCY_TARGET_PRESSURE_REWARD",
		"Amount",
		250
	),
	(
		"RELIGIOUS_EMERGENCY_TARGET_PRESSURE_REWARD",
		"Range",
		9
	);
	
```

