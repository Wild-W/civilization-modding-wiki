---
tags:
- EffectType
title: EFFECT_ADJUST_WAR_WEARINESS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_WAR_WEARINESS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Domestic `Boolean`
>	* Enemy `Boolean`
>	* Overall `Boolean`

## Samples

```SQL {title="GREATPERSON_JOAQUIM_MARQUES_LISBOA_ACTIVE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_JOAQUIM_MARQUES_LISBOA_ACTIVE",
		"MODIFIER_PLAYER_ADJUST_WAR_WEARINESS",
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
		"GREATPERSON_JOAQUIM_MARQUES_LISBOA_ACTIVE",
		"Amount",
		"-25"
	),
	(
		"GREATPERSON_JOAQUIM_MARQUES_LISBOA_ACTIVE",
		"Overall",
		1
	);
	
```


```SQL {title="DEFENSEOFMOTHERLAND_DOMESTICWARWEARINESS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DEFENSEOFMOTHERLAND_DOMESTICWARWEARINESS",
		"MODIFIER_PLAYER_ADJUST_WAR_WEARINESS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DEFENSEOFMOTHERLAND_DOMESTICWARWEARINESS",
		"Amount",
		"-100"
	),
	(
		"DEFENSEOFMOTHERLAND_DOMESTICWARWEARINESS",
		"Domestic",
		1
	);
	
```


```SQL {title="TRAIT_INCREASE_ENEMY_WAR_WEARINESS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_INCREASE_ENEMY_WAR_WEARINESS",
		"MODIFIER_PLAYER_ADJUST_WAR_WEARINESS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_INCREASE_ENEMY_WAR_WEARINESS",
		"Amount",
		100
	),
	(
		"TRAIT_INCREASE_ENEMY_WAR_WEARINESS",
		"Enemy",
		1
	);
	
```

