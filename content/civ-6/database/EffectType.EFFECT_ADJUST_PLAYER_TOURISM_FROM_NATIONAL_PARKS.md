---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TOURISM_FROM_NATIONAL_PARKS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TOURISM_FROM_NATIONAL_PARKS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="COMMEMORATION_TOURISM_GA_NATIONAL_PARKS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId
	)
VALUES
	(
		"COMMEMORATION_TOURISM_GA_NATIONAL_PARKS",
		"MODIFIER_PLAYER_ADJUST_TOURISM_FROM_NATIONAL_PARKS",
		"PLAYER_HAS_GOLDEN_AGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COMMEMORATION_TOURISM_GA_NATIONAL_PARKS",
		"Amount",
		100
	);
	
```

