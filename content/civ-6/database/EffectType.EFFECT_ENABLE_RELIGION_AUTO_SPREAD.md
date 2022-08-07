---
tags:
- EffectType
title: EFFECT_ENABLE_RELIGION_AUTO_SPREAD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ENABLE_RELIGION_AUTO_SPREAD
>
> * Class: `PLAYERS`
> * Parameters:
>	* Enable `Boolean`

## Samples
```SQL {title="RELIGIOUS_COLONIZATION_AUTO_SPREAD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RELIGIOUS_COLONIZATION_AUTO_SPREAD",
		"MODIFIER_PLAYER_RELIGION_ENABLE_AUTO_SPREAD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RELIGIOUS_COLONIZATION_AUTO_SPREAD",
		"Enable",
		1
	);
	
```

