---
tags:
- EffectType
title: EFFECT_PLAYER_DISCOVER_HERO
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_PLAYER_DISCOVER_HERO
>
> * Class: `Unknown`
> * Parameters:
>	* RandomHero `Unknown`

## Samples
```SQL {title="MODIFIER_DISCOVER_RANDOM_HERO"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"MODIFIER_DISCOVER_RANDOM_HERO",
		"MODIFIER_PLAYER_DISCOVER_HERO",
		1,
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
		"MODIFIER_DISCOVER_RANDOM_HERO",
		"RandomHero",
		1
	);
	
```

