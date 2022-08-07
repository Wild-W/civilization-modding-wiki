---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ALWAYS_FULL_RELIGIOUS_TOURISM
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ALWAYS_FULL_RELIGIOUS_TOURISM
>
> * Class: `PLAYERS`
> * Parameters:
>	* Enable `Boolean`

## Samples
```SQL {title="CRISTOREDENTOR_FULLRELIGIOUSTOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CRISTOREDENTOR_FULLRELIGIOUSTOURISM",
		"MODIFIER_PLAYER_ADJUST_ALWAYS_FULL_RELIGIOUS_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CRISTOREDENTOR_FULLRELIGIOUSTOURISM",
		"Enable",
		1
	);
	
```

