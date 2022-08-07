---
tags:
- EffectType
title: EFFECT_ADJUST_EXTRA_UNIT_COPY_TAG
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_EXTRA_UNIT_COPY_TAG
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* Tag `String`

## Samples
```SQL {title="VENETIAN_ARSENAL_EXTRANAVALMELEE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"VENETIAN_ARSENAL_EXTRANAVALMELEE",
		"MODIFIER_PLAYER_CITIES_ADJUST_EXTRA_UNIT_COPY_TAG"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"VENETIAN_ARSENAL_EXTRANAVALMELEE",
		"Amount",
		1
	),
	(
		"VENETIAN_ARSENAL_EXTRANAVALMELEE",
		"Tag",
		"CLASS_NAVAL_MELEE"
	);
	
```

