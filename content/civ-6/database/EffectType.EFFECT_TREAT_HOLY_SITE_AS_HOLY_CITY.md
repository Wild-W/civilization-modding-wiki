---
tags:
- EffectType
title: EFFECT_TREAT_HOLY_SITE_AS_HOLY_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_TREAT_HOLY_SITE_AS_HOLY_CITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Value `Integer`

## Samples
```SQL {title="MINOR_CIV_JERUSALEM_HOLY_SITE_UPGRADE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_JERUSALEM_HOLY_SITE_UPGRADE",
		"MODIFIER_PLAYER_TREAT_HOLY_SITES_AS_HOLY_CITIES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_JERUSALEM_HOLY_SITE_UPGRADE",
		"Value",
		1
	);
	
```

