---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_FREE_GREAT_PERSON_POINTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_FREE_GREAT_PERSON_POINTS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GREATPERSON_GREAT_PERSON_FREE_POINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GREAT_PERSON_FREE_POINTS",
		"MODIFIER_PLAYER_ADJUST_FREE_GREAT_PERSON_POINTS",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Type,
		Value
	)
VALUES
	(
		"GREATPERSON_GREAT_PERSON_FREE_POINTS",
		"Amount",
		"ScaleByGameSpeed",
		100
	);
	
```

