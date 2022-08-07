---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_BY_DOMAIN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_BY_DOMAIN
>
> * Class: `CITIES`
> * Parameters:
>	* UnitDomain `String`
>		* [UnitPromotionClasses.PromotionClassType]

## Samples

```SQL {title="GREAT_PERSON_JOSE_DE_SUCRE_SPAWN_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREAT_PERSON_JOSE_DE_SUCRE_SPAWN_UNIT",
		"MODIFIER_PLAYER_UNIT_GRANT_UNIT_BY_DOMAIN",
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
		"GREAT_PERSON_JOSE_DE_SUCRE_SPAWN_UNIT",
		"UnitDomain",
		"DOMAIN_LAND"
	);
	
```

