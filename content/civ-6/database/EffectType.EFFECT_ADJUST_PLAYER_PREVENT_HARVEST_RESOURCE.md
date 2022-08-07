---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_PREVENT_HARVEST_RESOURCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_PREVENT_HARVEST_RESOURCE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Enable `Boolean`

## Samples

```SQL {title="TRAIT_MAORI_PREVENT_HARVEST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_MAORI_PREVENT_HARVEST",
		"MODIFIER_PLAYER_ADJUST_PREVENT_HARVEST_RESOURCE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_MAORI_PREVENT_HARVEST",
		"Enable",
		1
	);
	
```

