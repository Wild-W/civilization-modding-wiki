---
tags:
- EffectType
title: EFFECT_ENABLE_UNIT_FAITH_PURCHASE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ENABLE_UNIT_FAITH_PURCHASE
>
> * Class: `CITIES`
> * Parameters:
>	* Tag `String`

## Samples

```SQL {title="TRAIT_NAVAL_MELEE_FAITH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_NAVAL_MELEE_FAITH",
		"MODIFIER_PLAYER_CITIES_ENABLE_UNIT_FAITH_PURCHASE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_NAVAL_MELEE_FAITH",
		"Tag",
		"CLASS_NAVAL_MELEE"
	);
	
```

