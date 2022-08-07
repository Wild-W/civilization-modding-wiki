---
tags:
- EffectType
title: EFFECT_ADJUST_SPACE_RACE_PROJECTS_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_SPACE_RACE_PROJECTS_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GREATPERSON_SPACE_RACE_PRODUCTION_RATE_LARGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		Permanent
	)
VALUES
	(
		"GREATPERSON_SPACE_RACE_PRODUCTION_RATE_LARGE",
		"MODIFIER_PLAYER_CITIES_ADJUST_SPACE_RACE_PROJECTS_PRODUCTION",
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
		"GREATPERSON_SPACE_RACE_PRODUCTION_RATE_LARGE",
		"Amount",
		100
	);
	
```

