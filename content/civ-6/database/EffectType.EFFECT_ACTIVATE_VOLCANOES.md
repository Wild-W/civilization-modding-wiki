---
tags:
- EffectType
title: EFFECT_ACTIVATE_VOLCANOES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ACTIVATE_VOLCANOES
>
> * Class: `Unknown`
> * Parameters:
>	* PercentageActive `Integer`

## Samples
```SQL {title="MEAGDISASTERS_MODE_ACTIVATE_VOLCANOES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MEAGDISASTERS_MODE_ACTIVATE_VOLCANOES",
		"MODIFIER_GAME_SET_ACTIVE_VOLCANOES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MEAGDISASTERS_MODE_ACTIVATE_VOLCANOES",
		"PercentageActive",
		100
	);
	
```

