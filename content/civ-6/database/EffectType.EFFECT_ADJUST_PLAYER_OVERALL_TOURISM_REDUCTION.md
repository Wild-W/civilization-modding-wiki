---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_OVERALL_TOURISM_REDUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_OVERALL_TOURISM_REDUCTION
>
> * Class: `PLAYERS`
> * Parameters:
>	* Modifier `Integer`

## Samples

```SQL {title="FUTURE_COUNTER_CULTURE_TOURISM_REDUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"FUTURE_COUNTER_CULTURE_TOURISM_REDUCTION",
		"MODIFIER_PLAYER_ADJUST_OVERALL_TOURISM_REDUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FUTURE_COUNTER_CULTURE_TOURISM_REDUCTION",
		"Modifier",
		20
	);
	
```

